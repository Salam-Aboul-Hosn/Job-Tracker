from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Job

class JobView(View):
    def get(self, request):
        records = Job.objects.all()
        data = [{'position': record.position,
                'company': record.company,
                'date_applied': record.date_applied,
                'compensation': record.compensation,
                'location': record.location,
                'level': record.level} for record in records]
        return JsonResponse(data, safe=False)


    def post(self, request):
        try:
            data = json.loads(request.body)
            position = data.get('position')
            company = data.get('company')
            date_applied = data.get('date_applied')
            compensation = data.get('compensation')
            location = data.get('location')
            level = data.get('level')

            # Only for the required fields
            if not all([position, company]):
                return JsonResponse({'error': 'These fields are required'}, status=400)

            new_record = Job(
                position=position,
                company=company,
                date_applied=date_applied,
                compensation=compensation,
                location=location,
                level=level
            )
            
            new_record.save()
            return JsonResponse({'message': 'Record created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
    

class JobWithIdView(View):
    def get(self, request, pk):  
        try:
            job = Job.objects.get(pk=pk)
            data = {
                'position': job.position,
                'company': job.company,
                'date_applied': job.date_applied,
                'compensation': job.compensation,
                'location': job.location,
                'level': job.level
            }
            return JsonResponse(data, status=200)
        except Job.DoesNotExist:
            return JsonResponse({'error': 'Job not found'}, status=404)
        
    def patch(self, request, pk, *args, **kwargs):  # Ensure 'pk' is included here
        try:
            data = json.loads(request.body)
            position = data.get('position')
            company = data.get('company')
            date_applied = data.get('date_applied')
            compensation = data.get('compensation')
            location = data.get('location')
            level = data.get('level')

            job_id = pk  # Use 'pk' directly from the method parameters
            if not job_id:
                return JsonResponse({'error': 'Job ID not provided'}, status=400)
            
            job = Job.objects.get(pk=job_id)
            if position:
                job.position = position
            if company:
                job.company = company
            if date_applied:
                job.date_applied = date_applied
            if compensation:
                job.compensation = compensation
            if location:
                job.location = location
            if level:
                job.level = level

            job.save()

            return JsonResponse({'message': 'Record updated successfully'}, status=200)
        except Job.DoesNotExist:
            return JsonResponse({'error': 'Job not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def delete(self, request, pk, *args, **kwargs):  # Ensure 'pk' is included here
        try:
            job_id = pk  # Use 'pk' directly from the method parameters
            if not job_id:
                return JsonResponse({'error': 'Job ID not provided'}, status=400)

            job = Job.objects.get(pk=job_id)
            job.delete()

            return JsonResponse({'message': 'Record deleted successfully'}, status=200)
        except Job.DoesNotExist:
            return JsonResponse({'error': 'Job not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
