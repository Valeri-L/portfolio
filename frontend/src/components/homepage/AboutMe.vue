<script setup>
import { ref, onMounted, watch, computed, nextTick } from 'vue'
import { useLanguage } from '../../composables/useLanguage'

const { lang, getText } = useLanguage()

const displayText = ref('')
const currentWordIndex = ref(0)
const currentLetterIndex = ref(0)
const isDeleting = ref(false)
const finishedTyping = ref(false)

const typingSpeed = 160
const deletingSpeed = 50
const pauseBetweenWords = 700

// Make words computed so it updates reactively on language change
const words = computed(() => [
  getText('aboutMe.title'),
  getText('aboutMe.name')
])

let typingTimeout

function startTypingAnimation() {
  clearTimeout(typingTimeout)
  if (finishedTyping.value) return

  const currentWord = words.value[currentWordIndex.value]

  if (!isDeleting.value) {
    displayText.value = currentWord.substring(0, currentLetterIndex.value + 1)
    currentLetterIndex.value++

    if (currentLetterIndex.value === currentWord.length) {
      if (currentWordIndex.value === 0) {
        typingTimeout = setTimeout(() => {
          isDeleting.value = true
          startTypingAnimation()
        }, pauseBetweenWords)
        return
      } else {
        finishedTyping.value = true
        return
      }
    }
  } else {
    displayText.value = currentWord.substring(0, currentLetterIndex.value - 1)
    currentLetterIndex.value--

    if (currentLetterIndex.value === 0) {
      isDeleting.value = false
      currentWordIndex.value++
    }
  }

  typingTimeout = setTimeout(startTypingAnimation, isDeleting.value ? deletingSpeed : typingSpeed)
}

function resetTyping() {
  clearTimeout(typingTimeout)
  displayText.value = ''
  currentWordIndex.value = 0
  currentLetterIndex.value = 0
  isDeleting.value = false
  finishedTyping.value = false
  // Wait for next DOM update to get new `words` before typing
  nextTick(() => {
    startTypingAnimation()
  })
}

onMounted(() => {
  setTimeout(()=>{
    startTypingAnimation()
  },900)
})

// Watch for language change and reset typing
watch(lang, () => {
  resetTyping()
})
</script>
<!-- border-2 border-borders-purple -->

<template>
  <div
    class="about-me-container relative  rounded-lg  "
    :dir="lang === 'he' ? 'rtl' : 'ltr'"
  >
    <!-- gradient lives behind everything -->
    <div class="sliding-gradient inset-0"></div>

    <!-- your actual content sits on top -->

    <div class="aboutMeContext">
      <h1 class="capitalize h-16 overflow-hidden flex items-center mb-10">
        {{ displayText }}<span class="typing-cursor ml-1"></span>
      </h1>
        <p
          class="mb-6"
          v-for="(paragraph, index) in getText('aboutMe.paragraphs')"
          :key="index"
          >
            {{ paragraph }}
          </p>
    </div>
  </div>
  
</template>




<style scoped>

@keyframes slideFromRight {
  0%  { opacity: 0;transform: translateX(20rem);}
  80% { transform: translateX(-5rem); }
  100% { opacity: 1;transform: translateX(0); }
}

@keyframes slideFromLeft {
  0%  { opacity: 0;transform: translateX(-20rem);}
  80% { transform: translateX(5rem); }
  100% { opacity: 1;transform: translateX(0); }
}

.sliding-gradient {
  position: absolute;
  background-color: rgba(199, 120, 221, 0.15);
  padding: 4rem;
  margin: 0 10rem;
  border: 3px solid rgba(199, 120, 221, 0.15);
  border-radius: .7rem;
  animation: slideFromRight 1.2s ease-in-out;
}

.aboutMeContext {
  color: #f2f2f2;
  z-index: 999;
  padding: 4rem;
  margin: 0 10rem;
  animation: slideFromLeft 1.2s ease-in-out;
}

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
