<template>
    <div class="flip-link-wrapper">
      <!-- flip-animated link/label text -->
      <a
        :href="copyable ? undefined : href"
        @click="onClick"
        class="flip-link"
        :target="copyable ? undefined : '_blank'"
        :rel="copyable ? undefined : 'noopener'"
      >
        <!-- front row of chars -->
        <div class="line front">
          <span
            v-for="(char, i) in letters"
            :key="`front-${i}`"
            class="char"
            :style="{ '--delay': `${i * stagger}s` }"
          >
            {{ char }}
          </span>
        </div>
        <!-- back row of chars -->
        <div class="line back">
          <span
            v-for="(char, i) in letters"
            :key="`back-${i}`"
            class="char"
            :style="{ '--delay': `${i * stagger}s` }"
          >
            {{ char }}
          </span>
        </div>
      </a>
  
      <!-- action hint: arrow vs clipboard icon + text -->
      <span
        class="action-icon"
        :class="copyable ? 'copy-icon' : 'arrow-icon'"
      >
        <template v-if="!copyable">
          Go To →
        </template>
        <template v-else>
          Copy to clipboard 📋
        </template>
      </span>
  
      <!-- “Copied!” feedback -->
      <span v-if="showCopied" class="copy-msg">Copied!</span>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  
  const props = defineProps({
    href:      String,
    label:     { type: String, required: true },
    copyable:  { type: Boolean, default: false },
    copyText:  { type: String, default: '' },    // what actually gets copied
    duration:  { type: Number, default: 0.25 },
    stagger:   { type: Number, default: 0.025 }
  })
  
  const showCopied = ref(false)
  
  // split the visible label into characters
  const letters = computed(() => props.label.split(''))
  
  function onClick(evt) {
    if (props.copyable) {
      evt.preventDefault()
      // copy either your explicit copyText or fallback to label
      console.log(props)
      const text = !props.copyText ? props.label : props.copyText
      navigator.clipboard.writeText(text)
      showCopied.value = true
      setTimeout(() => (showCopied.value = false), 2000)
    }
    // non-copyable: let the <a> navigate as normal
  }
  </script>
  
  <style scoped>
  .flip-link-wrapper {
    display: inline-flex;
    align-items: center;
    gap: 2rem;
    position: relative;
    overflow: visible;
  }
  
  .action-icon {
    font-size: 0.875rem;
    opacity: 0;
    transition: opacity 0.2s ease-in-out 0.3s;
  }
  .flip-link-wrapper:hover .action-icon {
    opacity: 1;
  }
  
  /* Copied confirmation */
  .copy-msg {
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translate(-50%, 0.5rem);
    background: rgba(0,0,0,0.75);
    color: #fff;
    padding: 0.25rem 0.5rem;
    border-radius: 0.25rem;
    font-size: 0.75rem;
    z-index: 10;
  }
  
  /* Flip animation */
  .flip-link {
    position: relative;
    overflow: hidden;
    display: inline-block;
    font-weight: 900;
    font-size: 3.6rem;
    line-height: 1.2;
    color: currentColor;
    cursor: pointer;
    text-decoration: none;
  }
  .flip-link .line {
    display: flex;
    white-space: nowrap;
  }
  .flip-link .front .char {
    transform: translateY(0);
    transition: transform var(--duration) ease-in-out var(--delay);
  }
  .flip-link .back {
    position: absolute;
    top: 0;
    left: 0;
  }
  .flip-link .back .char {
    transform: translateY(100%);
    transition: transform var(--duration) ease-in-out var(--delay);
  }
  .flip-link:hover .front .char {
    transform: translateY(-100%);
  }
  .flip-link:hover .back .char {
    transform: translateY(0);
  }
  
  /* control timing via CSS vars */
  .flip-link {
    --duration: 0.25s;
  }
  </style>
  