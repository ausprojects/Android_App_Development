import scrapy


class CoursesSpider(scrapy.Spider):
    name = "courses"

    # List of URLs to scrape
    start_urls = [
        "https://talentedge.com/ecornell/certificate-course-data-analytics-360",
        "https://talentedge.com/esgci-school-of-management-paris/doctorate-of-business-administration-esgci",
        "https://talentedge.com/iim-lucknow/advanced-program-in-strategic-management-for-business-excellence",
        "https://talentedge.com/iim-raipur/post-graduate-executive-certification-in-human-resource-management-iimr-hr",
        "https://talentedge.com/iim-kozhikode/professional-certificate-program-in-strategic-management",
        "https://talentedge.com/iim-raipur/certificate-course-strategic-management",
        "https://talentedge.com/iiit-allahabad/big-data-analytics-machine-learning-course-iiit-allahabad",
        "https://talentedge.com/iim-raipur/certificate-course-strategic-management",
        "https://talentedge.com/iiit-allahabad/machine-learning-and-big-data-analytics-for-professionals-with-prior-python-knowledge",
        "https://talentedge.com/goa-institute-of-management/exectuive-pg-program-in-health-care-management"
    ]

    def parse(self, response):
        # Extracting data
        course_data = {
            'course_link': response.url,
            'title': response.css('h1::text').get(),
            'description': response.css('div.description::text').get(),
            'durations': response.css('div.duration::text').get(),
            'timings': response.css('div.timing::text').get(),
            'course_start': response.css('div.start-date::text').get(),
            'what_you_will_study': response.css('div.study-content::text').get(),
            'skills': response.css('div.skills::text').get(),
            'target_students': response.css('div.target-students::text').get(),
            'prerequisite': response.css('div.prerequisite::text').get(),
            'contents': response.css('div.contents::text').get(),
            'Faculty Name': response.css('div.faculty::text').get(),
            'Institute Name': response.css('div.institute-name::text').get()
        }

        # Extract faculty names and descriptions
        faculty = response.css('div.faculty')
        for index, faculty_member in enumerate(faculty, start=1):
            course_data[f'Faculty Name {index}'] = faculty_member.css('h2::text').get()
            course_data[f'Faculty Description {index}'] = faculty_member.css('p::text').get()

        yield course_data