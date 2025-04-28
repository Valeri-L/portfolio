<script setup>
import { ref, onMounted } from 'vue'

defineProps({
  msg: String,
})

const displayText = ref('')
const words = ['About Me', 'Valeri Levinson']
const currentWordIndex = ref(0)
const currentLetterIndex = ref(0)
const isDeleting = ref(false)
const finishedTyping = ref(false)

// Speeds
const typingSpeed = 160; 
const deletingSpeed = 50; 
const pauseBetweenWords = 700; 

function startTypingAnimation() {
  if (finishedTyping.value) return;

  const currentWord = words[currentWordIndex.value];

  if (!isDeleting.value) {
    // Typing
    displayText.value = currentWord.substring(0, currentLetterIndex.value + 1);
    currentLetterIndex.value++;

    if (currentLetterIndex.value === currentWord.length) {
      // Finished typing current word
      if (currentWordIndex.value === 0) {
        // If it's "About Me", wait and delete
        setTimeout(() => {
          isDeleting.value = true;
          startTypingAnimation();
        }, pauseBetweenWords);
        return;
      } else {
        // If it's "Valeri Levinson", stop here
        finishedTyping.value = true;
        return;
      }
    }
  } else {
    // Deleting
    displayText.value = currentWord.substring(0, currentLetterIndex.value - 1);
    currentLetterIndex.value--;

    if (currentLetterIndex.value === 0) {
      // Finished deleting
      isDeleting.value = false;
      currentWordIndex.value++;
    }
  }

  setTimeout(startTypingAnimation, isDeleting.value ? deletingSpeed : typingSpeed);
}

onMounted(() => {
  startTypingAnimation();
})
</script>

<template>
  <div class="border-solid rounded-lg border-2 border-borders-purple bg-sections-about_me bg-opacity-10 p-2 lg:p-10 md:p-6">
    <h1 class="capitalize h-16 overflow-hidden flex items-center mb-10">
      {{ displayText }}
      <span class="typing-cursor ml-1"></span>
    </h1>

    <div class="ml-6 m-4 max-w-2xl">
      <p class="mb-6">Hi, I'm Valeri. I'm a Backend Developer with Full-Stack skills and a strong foundation in Python, Django, React, and modern technologies like AWS and Docker. I’m based in Bat-Yam, Israel, with extensive experience in networking.</p>
      <p class="mb-6">I’m incredibly passionate about backend engineering, web application development, and creating full-stack solutions that are both functional and visually intuitive. I thrive on building large and complex projects, designing with purpose, and coding with passion.</p>
      <p class="mb-6">In my free time, I enjoy solving LeetCode problems, enhancing my skills with new frameworks and technologies, and working on real-world applications like my CRM Project and Ticket Manager app.</p>
    </div>
  </div>
</template>

<style scoped>
  .typing-cursor {
    display: inline-block;
    width: 2px;
    height: 1.5em;
    background-color: #f2f2f2;
    margin-left: 4px;
    animation: blink 1.3s steps(1, start) infinite;
  }

  @keyframes blink {
    0%, 100% {
      opacity: 1;
    }
    50% {
      opacity: 0;
    }
  }
</style>
