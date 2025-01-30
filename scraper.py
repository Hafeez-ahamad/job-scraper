import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    salary = Column(Float)

# Create SQLite database
engine = create_engine('sqlite:///data/jobs.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Scrape job listings
def scrape_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Scrape job listings (adjust selectors based on the website)
    jobs = []
    for job in soup.find_all('div', class_='job-listing'):
        title = job.find('h2').text.strip()
        company = job.find('span', class_='company').text.strip()
        location = job.find('span', class_='location').text.strip()
        salary = job.find('span', class_='salary').text.strip()
        salary = float(salary.replace('$', '').replace(',', '')) if salary else None

        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'salary': salary,
        })

    return jobs

# Save jobs to the database
def save_jobs(jobs):
    for job in jobs:
        new_job = Job(
            title=job['title'],
            company=job['company'],
            location=job['location'],
            salary=job['salary'],
        )
        session.add(new_job)
    session.commit()

# Main function
if __name__ == '__main__':
    url = 'https://example-job-board.com/jobs'  # Replace with the actual URL
    jobs = scrape_jobs(url)
    save_jobs(jobs)
    print(f"Scraped and saved {len(jobs)} jobs.")
