# PROJECT:  USA Credit Utilization.

## Overview:
This project analyzes credit usage patterns and payment behavior across different age groups and occupations, including writers, musicians, lawyers, scientists, and more. The goal is to explore credit utilization and payment trends, providing key insights and visualizations to support data-driven decision-making.

## Project Details:
### Data Collection and Automation Workflow:
A critical part of the project involves automating the data collection and integration process to ensure real-time updates and reduce manual efforts. The automation is achieved using several key components:

- **Outlook:**
Outlook is leveraged to automatically segregate incoming emails that contain relevant credit usage and payment data. By setting up rules and filters, only the necessary emails are flagged and routed for further processing. This ensures that only pertinent data feeds into the system, making the process efficient and streamlined.

- **Power Automate:**
Power Automate plays a central role in automating the data flow. After the relevant emails are segregated in Outlook, Power Automate extracts the data from these emails and initiates the process of transferring it to a designated Google Drive folder. This eliminates the need for manual intervention, allowing the project to scale and handle large volumes of incoming data effortlessly.

- **Google Drive:**
Google Drive is used as the primary storage solution for holding the segregated data. Power Automate ensures that the data extracted from Outlook is deposited into specific folders within Google Drive, where it is stored securely and can be easily accessed by other systems.

- **Google Cloud Platform (GCP) API & Python:**
To establish a seamless connection between Google Drive and Power BI, the GCP API is utilized along with a Python script. This integration allows the project to pull the relevant data directly from Google Drive into Power BI for visualization and analysis. By using Python in conjunction with the GCP API, the data is loaded efficiently into Power BI without needing manual uploads, ensuring real-time data availability for the dashboard.

## Power BI Visualization
Once the data is loaded into Power BI, it is processed and visualized through interactive dashboards.
These visualizations help understand how various demographic and occupational factors influence credit behavior, enabling more informed decision-making.