import requests
from django.conf import settings



class LeetCodeAPIError(Exception):
    """Custom exception for LeetCode API errors."""
    def __init__(self, message="An error occurred while fetching data from the LeetCode API"):
        super().__init__(message)


class APIFetch:
    # LeetCode GraphQL API endpoint and query
    LEETCODE_API_URL = settings.LEETCODE_API_URL

    # Query to fetch recent submissions
    RECENT_SUBMISSIONS_QUERY = """
    {
    recentAcSubmissionList(username: "hayhuhin", limit: 100) {
        title
        titleSlug
        timestamp
        statusDisplay
        lang
    }
    }
    """

    # Query to fetch problem details
    PROBLEM_DETAILS_QUERY = """
    query GetProblemDetails($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        title
        difficulty
        acRate
    }
    }
    """


    
    @staticmethod
    def fetch_leetcode_data():
        # Step 1: Fetch recent submissions
        try:
            response = requests.post(
                APIFetch.LEETCODE_API_URL, 
                json={"query": APIFetch.RECENT_SUBMISSIONS_QUERY}
            )
            response.raise_for_status()
            recent_data = response.json().get("data", {}).get("recentAcSubmissionList", [])

            # Initialize counters for difficulty levels
            difficulty_totals = {"Easy": 0, "Medium": 0, "Hard": 0}
            completed_questions = []

            # Step 2: Fetch details for each submission
            for submission in recent_data:
                title_slug = submission["titleSlug"]
                variables = {"titleSlug": title_slug}
                problem_response = requests.post(
                    APIFetch.LEETCODE_API_URL,
                    json={"query": APIFetch.PROBLEM_DETAILS_QUERY, "variables": variables}
                )
                problem_response.raise_for_status()
                problem_data = problem_response.json().get("data", {}).get("question", {})

                if problem_data:
                    difficulty = problem_data["difficulty"]
                    difficulty_totals[difficulty] += 1  # Increment difficulty counter
                    completed_questions.append({
                        "title": problem_data["title"],
                        "difficulty": difficulty,
                        "acRate": round(problem_data.get("acRate")),
                    })

            # Step 3: Return aggregated data
            result = {
                "completed_questions": completed_questions,
                "difficulty_totals": difficulty_totals,
            }
            return result

        except requests.exceptions.RequestException as e:
            raise LeetCodeAPIError(f"Error occurred: {e}")
    
