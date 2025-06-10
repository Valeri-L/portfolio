<template>
    <button
      @mouseenter="scramble"
      @mouseleave="stopScramble"
      :disabled="disabled"
      class="encrypt-btn"
    >
      <!-- gradient overlay slides on hover -->
      <span class="gradient-overlay"></span>
  
      <!-- button content: icon + dynamic text -->
      <div class="content">
        <span class="lock-icon">🔒</span>
        <span>{{ displayText }}</span>
      </div>
    </button>
  </template>
  
  <script setup>
  import { ref, onBeforeUnmount } from 'vue'
  
  // Props for customizable button text and shuffle behavior
  const props = defineProps({
    /**
     * The text to display and eventually reveal
     */
    targetText: {
      type: String,
      default: 'Encrypt data'
    },
    /** How many scramble cycles per letter */
    cyclesPerLetter: {
      type: Number,
      default: 2
    },
    /** Milliseconds between each shuffle update */
    shuffleTime: {
      type: Number,
      default: 50
    },
    /** Characters to pick from when scrambling */
    chars: {
      type: String,
      default: '!@#$%^&*():{};|,.<>/?'
    }
  })
  
  // Reactive display text state
  const displayText = ref(props.targetText)
  // Disabled while scrambling
  const disabled = ref(false)
  // Internal interval ID
  let intervalId = null
  
  function scramble() {
    let pos = 0
    disabled.value = true
  
    intervalId = setInterval(() => {
      displayText.value = props.targetText
        .split('')
        .map((ch, i) => {
          // if enough cycles passed, reveal actual letter
          if (pos / props.cyclesPerLetter > i) {
            return ch
          }
          // otherwise pick random
          const idx = Math.floor(Math.random() * props.chars.length)
          return props.chars[idx]
        })
        .join('')
  
      pos++
      if (pos >= props.targetText.length * props.cyclesPerLetter) {
        stopScramble()
      }
    }, props.shuffleTime)
  }
  
  function stopScramble() {
    clearInterval(intervalId)
    intervalId = null
    displayText.value = props.targetText
    disabled.value = false
  }
  
  onBeforeUnmount(() => {
    clearInterval(intervalId)
  })
  </script>
  
  <style scoped>
  .encrypt-btn {
    position: relative;
    overflow: hidden;
    border: 1px solid #4b5563;     /* neutral-500 */
    background: #374151;           /* neutral-700 */
    color: #d1d5db;                /* neutral-300 */
    font-family: monospace;
    text-transform: uppercase;
    padding: 0.5em 1em;
    border-radius: 0.5rem;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: transform 0.1s, color 0.2s;
  }
  .encrypt-btn:hover {
    transform: scale(1.025);
    color: #818cf8;                /* indigo-300 */
  }
  .encrypt-btn:active {
    transform: scale(0.975);
  }
  
  .gradient-overlay {
    pointer-events: none;
    position: absolute;
    inset: 0;
    z-index: 0;
    background: linear-gradient(
      to top,
      rgba(99, 102, 241, 0) 40%,
      rgba(99, 102, 241, 1) 50%,
      rgba(99, 102, 241, 0) 60%
    );
    transform: translateY(100%);
    opacity: 0;
    transition: opacity 0.2s;
  }
  .encrypt-btn:hover .gradient-overlay {
    opacity: 1;
    animation: slide-gradient 1s linear infinite alternate-reverse;
  }
  
  .content {
    position: relative;
    z-index: 1;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
  }
  
  .lock-icon {
    font-size: 1.2em;
  }
  
  @keyframes slide-gradient {
    to { transform: translateY(-100%); }
  }
  </style>
  