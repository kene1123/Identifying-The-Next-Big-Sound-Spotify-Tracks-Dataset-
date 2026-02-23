Identifying-Next-Big-Sound

End-to-end music analytics project analyzing streaming data to identify the types of songs a record label should prioritize for upcoming artist signings.

Project Overview

A mid-size record label is planning next quarter’s signings and needs data-driven guidance on what kind of music is most likely to succeed in today’s market.

This project analyzes large-scale streaming data from Spotify to uncover patterns in popularity across eras, genres, song characteristics, and audio features.

The goal is to support smarter signing decisions by identifying commercially successful music profiles.

Tools & Technologies

Python (Pandas, Jupyter Notebook) — Data cleaning & preprocessing
Power BI — Analysis, DAX measures, dashboard development
Kaggle Dataset — Data source

Repository Structure
The repository was structured to document analytics flow throughout the project.
C:.
│   str.txt
│   
├───Data
│   ├───Cleaned
│   │       Tracks_cleaned.csv
│   │       
│   └───Raw
│           Artists.csv
│           tracks.csv
│           
├───Power Bi
│   └───Report
│           SpotifyReport.pdf
│           
├───Python
│   └───Cleaning Script
│           Spotify_Project.html
│           Spotify_Project.py
│           
└───Word Documentation
        Mini Project.docx
        
Business Objectives

The analysis aims to answer one key question:
What kind of music should the label be betting on right now?

Specifically, the project evaluates:
•	Which musical eras perform best
•	Whether vocal or instrumental tracks dominate
•	Audio features linked to hit potential
•	Optimal track duration for popularity
•	High-performing genres in the current market

Dataset

Source: Kaggle — Spotify Tracks and Artists Dataset
Tracks dataset (initial state)

Rows: 586,672

Columns: 20

Missing values: None

Duplicate IDs: None

Data types: String, integer, decimal

Data Preparation & Cleaning

Data cleaning was performed in Python using Pandas within Jupyter Notebook.

Key transformations
•	Converted track duration from milliseconds to minutes (duration_minutes)
•	Standardized release dates into proper date format (release_date1)
•	Rounded decimal fields to 2 decimal places
•	Trimmed whitespace and standardized text formatting
•	Merged genre information from the artists dataset
•	Filled missing genres with "Unknown"

Removed unused columns:
•	id_artists
•	release_date
•	name_y
•	duration_ms

After intermediate transformations increased row count, duplicate rows were removed to restore dataset integrity.

Analytical Approach

Exploratory analysis and visualization were conducted in Power BI to identify patterns linked to commercial success.

Feature Engineering & Segmentation:
-	Musical Eras: Classic, Old School, 2000s (Y2K)
-	Instrumentalness:
Low - Vocal-dominant tracks
High - Instrumental-heavy tracks
-	Hit Potential Score: Derived from danceability and energy
-	Duration Groups: Categorized to evaluate impact on popularity
-	Genre Performance: Top genres above overall popularity average

Key Insights
•	Modern (2000s-era) tracks show the highest popularity
•	Vocal-driven songs outperform instrumental tracks
•	High-energy, danceable songs have the strongest hit potential
•	Tracks between 3–5 minutes perform best
•	Pop-oriented genres dominate high-performance categories

Recommendations for Next-Quarter Signings

Based on the analysis, the label should prioritize artists who produce:
•	Contemporary, modern-sounding music
•	Strong vocal performances
•	High-energy, danceable tracks
•	Songs within standard commercial length (3–5 minutes)
•	Music in proven high-demand genres like pop
This strategy reduces risk and aligns signings with current listener preferences.

Deliverables

Cleaned and enriched dataset
Power BI dashboard for exploratory insights
Business recommendations for talent acquisition

Business Value

This project demonstrates how streaming data can guide strategic decisions in the music industry by:
•	Reducing reliance on intuition in artist signings
•	Identifying commercially viable music characteristics
•	Supporting evidence-based talent acquisition
•	Improving probability of successful releases

Conclusion

Current listener behavior favors modern, vocal-focused, high-energy music with broad appeal. Signing artists who align with these characteristics increases the likelihood of commercial success in the upcoming quarter.
