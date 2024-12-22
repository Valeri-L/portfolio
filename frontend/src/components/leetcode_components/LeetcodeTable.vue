<template>
    <div class="leetcode-table">
        <div class="mb-6 ">
            <h3 class="capitalize pb-1">leetcode</h3>
            <p class="pb-2 pl-2">problems i solved</p>

        </div>
      <div class="xl:h-[440px] lg:h-[540px] md:h-[540px]  sm:h-[400px]">

          <table>
              <thead>
                <tr class="border-b border-borders-grey border-opacity-50">
                  <th class="title-col">Title</th>
                  <!-- <th class="solution-col">Solution</th> -->
                  <th class="acceptance-col">Acceptance</th>
                  <th class="difficulty-col">Difficulty</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(question, index) in currentQuestions" :key="index"
                :class="index % 2 === 0 ? 'bg-table-dark' : 'bg-table-medium'"
                >
                  <td class="title-col">{{ question.title }}</td>
                  <td class="acceptance-col">{{ question.acRate }}%</td>
                  <td :class="[
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
        <a
          @click="previousPage"
          aria-label="previous"
          class="pagination-btn"
          :class="{ 'disabled': currentPage === 1 }"
        >
          <img src="/arrow_left.svg" alt="previous" class="w-6 h-6" />
        </a>
        <span class="page-info">{{ currentPage }} / {{ totalPages }}</span>
        <a
          @click="nextPage"
          aria-label="next"
          class="pagination-btn"
          :class="{ 'disabled': currentPage === totalPages }"
        >
          <img src="/arrow_right.svg" alt="next" class="w-6 h-6" />
        </a>
      </div>

      </div>
  </template>

  
<script setup>
import { ref, computed } from 'vue';

// Props for questions data
const props = defineProps({
  questions: {
    type: Array,
    required: true,
  },
});

// Reactive states
const currentPage = ref(1);
const itemsPerPage = ref(6); // Adjust this value to control the number of rows per page

// Computed property for paginated questions
const totalPages = computed(() => Math.ceil(props.questions.length / itemsPerPage.value));
const currentQuestions = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  const end = start + itemsPerPage.value;
  return props.questions.slice(start, end);
});

// Pagination methods
const previousPage = () => {
  if (currentPage.value > 1) {
    currentPage.value -= 1;
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value += 1;
  }
};
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
  