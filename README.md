# Content-Based Book Recommendation System

A modular, content-based recommendation engine developed for the **Data Structures and Algorithms (DSA)** course. This system suggests books based on a user's reading history and explicit genre preferences using similarity functions.

## Overview
This project implements a system that analyzes book genres to generate personalized recommendations. Unlike collaborative filtering, it does not require ratings from other users; instead, it leverages a **Weighted User Profile** and **Genre Similarity** to rank books.

## Objectives
* Design and implement a content-based recommendation system.
* Apply DSA concepts: **Dictionaries, Hash Maps, Sets, and Sorting algorithms**.
* Create a **weighted user profile** based on reading history.
* Provide an interactive system with **explicit genre boosts**.

## Data Structures Used
* **Hash Maps / Dictionaries**: Used to store user profiles and handle genre frequency counting.
* **Sets**: Used for rapid intersection between book genres and user preferences.
* **Lists**: Used to store the collection of books and the final generated recommendations.

## Tech Stack
* **Language**: Python
* **Libraries**: `pandas` (data framing), `ast` (literal evaluation of genre strings
* **Tools**: VS Code, Numbers (for CSV cleaning)

## Logic & Methodology
1.  **Data Preprocessing**: The system reads `bookSet.csv` and converts genre strings into Python sets for efficient processing.
2.  **Weighted Profile**: Each genre is assigned a weight based on how many times it appears in the user's reading history.
3.  **Similarity Calculation**:
    * **Base Score**: Sum of overlapping genre weights divided by total profile weight.
    * **Genre Query Boost**: An additional score added if the book matches genres manually entered by the user.
4.  **Ranking**: The system excludes already-read books, sorts the remaining list by the final score, and returns the top-N results.

## Database Description
The system utilizes a `bookSet.csv` file containing:
* **Title**: Name of the book. 
* **Author**: Name of the author. 
* **Description**: Book summary.
* **Genres**: List of associated genres.
* **Cover**: URL for the book cover image.
