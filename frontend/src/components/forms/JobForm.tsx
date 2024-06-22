import React, { useState, ChangeEvent, FormEvent } from 'react';
import axios from 'axios';

// Define TypeScript interface for job details
interface JobFormData {
  position: string;
  company: string;
  date_applied?: string; // Optional field
  compensation?: string; // Optional field
  location?: string; // Optional field
  level?: string; // Optional field
}

const JobForm: React.FC = () => {
  const [formData, setFormData] = useState<JobFormData>({
    position: '',
    company: '',
    date_applied: '',
    compensation: '',
    location: '',
    level: '',
  });

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/api/job/',
        formData
      );
      console.log(response.data);
      setFormData({
        position: '',
        company: '',
        date_applied: '',
        compensation: '',
        location: '',
        level: '',
      });
    } catch (error) {
      console.error('Error submitting job:', error);
    }
  };
  console.log(formData);

  return (
    <div>
      <h2>Add a New Job</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor='position'>Position:</label>
          <input
            type='text'
            id='position'
            name='position'
            value={formData.position}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor='company'>Company:</label>
          <input
            type='text'
            id='company'
            name='company'
            value={formData.company}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor='date_applied'>Date Applied:</label>
          <input
            type='date'
            id='date_applied'
            name='date_applied'
            value={formData.date_applied}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor='compensation'>Compensation:</label>
          <input
            type='text'
            id='compensation'
            name='compensation'
            value={formData.compensation}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor='location'>Location:</label>
          <input
            type='text'
            id='location'
            name='location'
            value={formData.location}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor='level'>Level:</label>
          <input
            type='text'
            id='level'
            name='level'
            value={formData.level}
            onChange={handleChange}
          />
        </div>
        <button type='submit'>Submit</button>
      </form>
    </div>
  );
};

export default JobForm;
