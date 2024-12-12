<template>
    <div class="leetcode-table">
        <div class="mb-6 border-b border-borders-green border-opacity-50">
            <h3 class="capitalize">leetcode</h3>
            <p class="">leetcode questions that i solved</p>

        </div>
    <div class="lg:h-auto md:h-auto sm:h-[600px]">
      <table >
        <thead>
          <tr class="border-b border-borders-grey border-opacity-50">
            <th class="title-col">Title</th>
            <th class="solution-col">Solution</th>
            <th class="acceptance-col">Acceptance</th>
            <th class="difficulty-col">Difficulty</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(question, index) in currentQuestions" :key="index"
          :class="index % 2 === 0 ? 'bg-table-dark' : 'bg-table-medium'"
          >
            <td class="title-col">{{ question.title }}</td>
            <td class="solution-col">
                <a :href="question.solution" target="_blank" aria-label="GitHub" class="hover:text-gray-400">
                    <img src="/file.svg" alt="GitHub" class="w-6 h-6" >
                </a>
            </td>
            <td class="acceptance-col">{{ question.acceptance }}</td>
            <td 
                :class="[
                    'difficulty-col ',
                    lower_case_difficulty = question.difficulty.toLowerCase(),
                    lower_case_difficulty === 'easy' ? 'text-text-green' :'', 
                    lower_case_difficulty === 'medium' ? 'text-text-yellow' :'', 
                    lower_case_difficulty === 'hard' ? 'text-text-red' :'', 
                    ]"
                >{{ question.difficulty }}</td>
          </tr>
        </tbody>
      </table>
    </div>
      <div class="pagination-buttons">
        <a @click="previousPage" aria-label="previous" class="pagination-btn">
            <img src="/arrow_left.svg" alt="previous" class="w-6 h-6" >
        </a>
        <a @click="nextPage" aria-label="next" class="pagination-btn">
            <img src="/arrow_right.svg" alt="next" class="w-6 h-6" >
        </a>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  
  const questions = ref(
    [
        { "title": "Two Sum", "solution": "#", "acceptance": "45%", "difficulty": "Easy" },
        { "title": "Add Two Numbers", "solution": "#", "acceptance": "37%", "difficulty": "Medium" },
        { "title": "Longest Substring Without Repeating Characters", "solution": "#", "acceptance": "31%", "difficulty": "Hard" },
        { "title": "Median of Two Sorted Arrays", "solution": "#", "acceptance": "29%", "difficulty": "Hard" },
        { "title": "Longest Palindromic Substring", "solution": "#", "acceptance": "26%", "difficulty": "Medium" },
        { "title": "Zigzag Conversion", "solution": "#", "acceptance": "34%", "difficulty": "Medium" },
        { "title": "Reverse Integer", "solution": "#", "acceptance": "42%", "difficulty": "Easy" },
        { "title": "String to Integer (atoi)", "solution": "#", "acceptance": "16%", "difficulty": "Medium" },
        { "title": "Palindrome Number", "solution": "#", "acceptance": "48%", "difficulty": "Easy" },
        { "title": "Container With Most Water", "solution": "#", "acceptance": "39%", "difficulty": "Medium" },
        { "title": "Roman to Integer", "solution": "#", "acceptance": "57%", "difficulty": "Easy" },
        { "title": "Longest Common Prefix", "solution": "#", "acceptance": "41%", "difficulty": "Easy" },
        { "title": "3Sum", "solution": "#", "acceptance": "28%", "difficulty": "Medium" },
        { "title": "Letter Combinations of a Phone Number", "solution": "#", "acceptance": "50%", "difficulty": "Medium" },
        { "title": "Valid Parentheses", "solution": "#", "acceptance": "38%", "difficulty": "Easy" },
        { "title": "Merge Two Sorted Lists", "solution": "#", "acceptance": "56%", "difficulty": "Easy" },
        { "title": "Generate Parentheses", "solution": "#", "acceptance": "58%", "difficulty": "Medium" },
        { "title": "Remove Nth Node From End of List", "solution": "#", "acceptance": "39%", "difficulty": "Medium" },
        { "title": "Swap Nodes in Pairs", "solution": "#", "acceptance": "45%", "difficulty": "Medium" },
        { "title": "Reverse Nodes in k-Group", "solution": "#", "acceptance": "34%", "difficulty": "Hard" },
        { "title": "Two Sum", "solution": "#", "acceptance": "45%", "difficulty": "Easy" },
        { "title": "Add Two Numbers", "solution": "#", "acceptance": "37%", "difficulty": "Medium" },
        { "title": "Longest Substring Without Repeating Characters", "solution": "#", "acceptance": "31%", "difficulty": "Hard" },
        { "title": "Median of Two Sorted Arrays", "solution": "#", "acceptance": "29%", "difficulty": "Hard" },
        { "title": "Longest Palindromic Substring", "solution": "#", "acceptance": "26%", "difficulty": "Medium" },
        { "title": "Zigzag Conversion", "solution": "#", "acceptance": "34%", "difficulty": "Medium" },
        { "title": "Reverse Integer", "solution": "#", "acceptance": "42%", "difficulty": "Easy" },
        { "title": "String to Integer (atoi)", "solution": "#", "acceptance": "16%", "difficulty": "Medium" },
        { "title": "Palindrome Number", "solution": "#", "acceptance": "48%", "difficulty": "Easy" },
        { "title": "Container With Most Water", "solution": "#", "acceptance": "39%", "difficulty": "Medium" },
        { "title": "Roman to Integer", "solution": "#", "acceptance": "57%", "difficulty": "Easy" },
        { "title": "Longest Common Prefix", "solution": "#", "acceptance": "41%", "difficulty": "Easy" },
        { "title": "3Sum", "solution": "#", "acceptance": "28%", "difficulty": "Medium" },
        { "title": "Letter Combinations of a Phone Number", "solution": "#", "acceptance": "50%", "difficulty": "Medium" },
        { "title": "Valid Parentheses", "solution": "#", "acceptance": "38%", "difficulty": "Easy" },
        { "title": "Merge Two Sorted Lists", "solution": "#", "acceptance": "56%", "difficulty": "Easy" },
        { "title": "Generate Parentheses", "solution": "#", "acceptance": "58%", "difficulty": "Medium" },
        { "title": "Remove Nth Node From End of List", "solution": "#", "acceptance": "39%", "difficulty": "Medium" },
        { "title": "Swap Nodes in Pairs", "solution": "#", "acceptance": "45%", "difficulty": "Medium" },
]

  );
  
  const currentPage = ref(0);
  const pageSize = 10;
  
  const currentQuestions = computed(() =>
    questions.value.slice(currentPage.value * pageSize, (currentPage.value + 1) * pageSize)
  );
  
  const hasPreviousPage = computed(() => currentPage.value > 0);
  
  const hasNextPage = computed(() =>
    (currentPage.value + 1) * pageSize < questions.value.length
  );
  
  function nextPage() {
    if (hasNextPage.value) {
      currentPage.value++;
    }
  }
  
  function previousPage() {
    if (hasPreviousPage.value) {
      currentPage.value--;
    }
  }
  </script>
  
  <style scoped>
  .leetcode-table {
    width: 100%;
    border-collapse: collapse;
  }
  
  table {
    width: 100%;
    border-spacing: 0;
  }
  
  th,
  td {
    text-align: left;
    padding: 12px 16px;
  }
  
  th {
    font-weight: bold;
  }
  
  /* Adjust column widths */
  .title-col {
    width: 45%;
    align-items:"center;"
  }
  
  .solution-col {
    width: 20%;
  }
  
  .acceptance-col {
    width: 15%;
  }
  
  .difficulty-col {
    width: 20%;
  }
  
  /* Pagination Buttons */
  .pagination-buttons {
    margin-top: 10px;
    width:auto;
    display: flex;
    justify-content: center;
    gap: 10px;
  }
  
  .pagination-btn {
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .pagination-btn:hover {
    /* background-color: #2d3748; */
    transform: scale(1.1); /* Scale up slightly */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Add a subtle shadow */
  }
  </style>
  