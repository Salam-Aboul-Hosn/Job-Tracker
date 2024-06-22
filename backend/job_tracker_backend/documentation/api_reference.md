# JobView and JobWithIdView Documentation

## Overview
This module defines two Django class-based views: `JobView` and `JobWithIdView`. These views handle CRUD operations for `Job` model instances, utilizing JSON for request and response bodies.

## JobView

### Description
`JobView` handles HTTP GET and POST requests for the `Job` model.

### Methods

#### GET
- **URL**: `/jobs/`
- **Description**: Retrieves all job records.
- **Response**:
  - Status: `200 OK`
  - Body: JSON array of job records.

#### POST
- **URL**: `/jobs/`
- **Description**: Creates a new job record.
- **Request Body**:
  - `position` (required): string
  - `company` (required): string
  - `date_applied` (optional): string
  - `compensation` (optional): integer
  - `location` (optional): string
  - `level` (optional): string
- **Response**:
  - Status: `201 Created`
  - Body: `{"message": "Record created successfully"}`
- **Error Responses**:
  - Status: `400 Bad Request`
  - Body: `{"error": "These fields are required"}` if required fields are missing.
  - Status: `400 Bad Request`
  - Body: `{"error": "Invalid JSON"}` if JSON is malformed.

## JobWithIdView

### Description
`JobWithIdView` handles HTTP GET, PATCH, and DELETE requests for a single `Job` model instance specified by its primary key (`pk`).

### Methods

#### GET
- **URL**: `/jobs/<pk>/`
- **Description**: Retrieves a job record by its primary key.
- **Response**:
  - Status: `200 OK`
  - Body: JSON object of the job record.
- **Error Responses**:
  - Status: `404 Not Found`
  - Body: `{"error": "Job not found"}` if the job does not exist.

#### PATCH
- **URL**: `/jobs/<pk>/`
- **Description**: Updates fields of a job record specified by its primary key.
- **Request Body**: JSON object with any of the fields to update:
  - `position` (optional): string
  - `company` (optional): string
  - `date_applied` (optional): string
  - `compensation` (optional): integer
  - `location` (optional): string
  - `level` (optional): string
- **Response**:
  - Status: `200 OK`
  - Body: `{"message": "Record updated successfully"}`
- **Error Responses**:
  - Status: `404 Not Found`
  - Body: `{"error": "Job not found"}` if the job does not exist.
  - Status: `400 Bad Request`
  - Body: `{"error": "Invalid JSON"}` if JSON is malformed.
  - Status: `500 Internal Server Error`
  - Body: `{"error": "<error message>"}` for any other errors.

#### DELETE
- **URL**: `/jobs/<pk>/`
- **Description**: Deletes a job record specified by its primary key.
- **Response**:
  - Status: `200 OK`
  - Body: `{"message": "Record deleted successfully"}`
- **Error Responses**:
  - Status: `404 Not Found`
  - Body: `{"error": "Job not found"}` if the job does not exist.
  - Status: `500 Internal Server Error`
  - Body: `{"error": "<error message>"}` for any other errors.

## Models

### Job
- `position` (required): `CharField(max_length=50)`
- `company` (required): `CharField(max_length=100)`
- `date_applied` (optional): `CharField(max_length=50, blank=True, null=True)`
- `compensation` (optional): `IntegerField(blank=True, null=True)`
- `location` (optional): `CharField(max_length=50, blank=True, null=True)`
- `level` (optional): `CharField(max_length=50, blank=True, null=True)`

## Usage

### Import Statements
```python
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Job
