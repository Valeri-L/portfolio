<template>
    <div ref="containerRef" :class="['scroll-reveal', containerClassName]">
      <p :class="['scroll-reveal-text', textClassName]">
        <template v-for="(token, idx) in tokens" :key="idx">
          <span v-if="/\s+/.test(token)">{{ token }}</span>
          <span v-else class="word">{{ token }}</span>
        </template>
      </p>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted, onBeforeUnmount, watch } from 'vue'
  import { gsap } from 'gsap'
  
  // Props
  const props = defineProps({
    /** Text to reveal */
    text: { type: String, default: '' },
    /** Delay before reveal (ms) */
    delay: { type: Number, default: 300 },
    /** Word animation duration (s) */
    duration: { type: Number, default: 0.6 },
    /** GSAP easing */
    ease: { type: String, default: 'power2.out' },
    /** Stagger between words (s) */
    stagger: { type: Number, default: 0.05 },
    /** Y offset (px) start position */
    yOffset: { type: Number, default: 20 },
    /** Apply blur during reveal */
    enableBlur: { type: Boolean, default: false },
    /** Blur strength (px) */
    blurStrength: { type: Number, default: 4 },
    /** IntersectionObserver threshold */
    threshold: { type: Number, default: 0.2 },
    /** Classes on container */
    containerClassName: { type: String, default: '' },
    /** Classes on text */
    textClassName: { type: String, default: '' }
  })
  
  const containerRef = ref(null)
  let observer
  
  // split text into words & whitespace
  const tokens = computed(() => (props.text || '').split(/(\s+)/))
  
  onMounted(() => {
    observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          observer.unobserve(containerRef.value)
          // after delay, animate the words
          setTimeout(() => {
            const words = containerRef.value.querySelectorAll('.word')
            gsap.set(words, {
              opacity: 0,
              y: props.yOffset,
              filter: props.enableBlur ? `blur(${props.blurStrength}px)` : 'none'
            })
            gsap.to(words, {
              opacity: 1,
              y: 0,
              filter: props.enableBlur ? 'blur(0px)' : 'none',
              duration: props.duration,
              ease: props.ease,
              stagger: props.stagger
            })
          }, props.delay)
        }
      },
      { threshold: props.threshold }
    )
    if (containerRef.value) observer.observe(containerRef.value)
  })
  
  onBeforeUnmount(() => {
    if (observer) observer.disconnect()
  })
  </script>
  
  <style scoped>
  .scroll-reveal {
    overflow: hidden;
  }
  .scroll-reveal-text {
    display: inline-block;
  }
  .word {
    display: inline-block;
    white-space: pre;
  }
  </style>