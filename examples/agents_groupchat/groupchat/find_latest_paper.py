# filename: find_latest_paper.py
import arxiv

# Define the query parameters for the search
search = arxiv.Search(
  query = "GPT-4",
  max_results = 1,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

# Perform the search and print the title and summary of the most recent paper
for result in search.results():
    print(f"Title: {result.title}\n\nSummary: {result.summary}\nURL: {result.entry_id}")