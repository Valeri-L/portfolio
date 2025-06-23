<!-- src/components/ScrollFloat.vue -->
<template>
    <h2
      ref="containerRef"
      :class="['scroll-float', containerClassName]"
    >
      <span :class="['scroll-float-text', textClassName]">
        <span
          v-for="(char, i) in chars"
          :key="i"
          class="char"
        >
          {{ char === ' ' ? '\u00A0' : char }}
        </span>
      </span>
    </h2>
  </template>
  
  <script setup>
  import { ref, computed, onMounted, watch } from 'vue'
  import { gsap } from 'gsap'
  import { ScrollTrigger } from 'gsap/ScrollTrigger'

  
  gsap.registerPlugin(ScrollTrigger)
  
  // ——— Props ——————————————————————————————————————————————————————————————————
  const props = defineProps({
    /**
     * The text to split/animate.  e.g. "What I Do"
     */
    text: {
      type: String,
      required: true
    },
    /**
     * If you want to use a custom scroller element (e.g. a scrollable div), pass a ref to it.
     * Otherwise the window is used.
     */
    scrollContainerRef: {
      type: Object,
      default: null
    },
    containerClassName: { type: String, default: '' },
    textClassName:      { type: String, default: '' },
    animationDuration:  { type: Number, default: 1 },
    ease:               { type: String, default: 'back.inOut(2)' },
    scrollStart:        { type: String, default: 'center bottom+=50%' },
    scrollEnd:          { type: String, default: 'bottom bottom-=40%' },
    stagger:            { type: Number, default: 0.03 }
  })
  
  // ——— Refs & Computed —————————————————————————————————————————————————————
  const containerRef = ref(null)
  
  /** break the text into an array of characters */
  const chars = computed(() => props.text.split(''))
  
  // ——— Lifecycle —————————————————————————————————————————————————————————————————
  onMounted(() => {
    const el = containerRef.value
    if (!el) return
  
    // if a scrollContainerRef is passed and has a `.value`, use that, otherwise window
    const scroller =
      props.scrollContainerRef && props.scrollContainerRef.value
        ? props.scrollContainerRef.value
        : window
  
    // select all the per-character spans
    const charEls = el.querySelectorAll('.char')
  
    gsap.fromTo(
      charEls,
      {
        willChange: 'opacity, transform',
        opacity: 0,
        yPercent: 120,
        scaleY: 2.3,
        scaleX: 0.7,
        transformOrigin: '50% 0%'
      },
      {
        duration: props.animationDuration,
        ease: props.ease,
        opacity: 1,
        yPercent: 0,
        scaleY: 1,
        scaleX: 1,
        stagger: props.stagger,
        scrollTrigger: {
          trigger: el,
          scroller,
          start: props.scrollStart,
          end: props.scrollEnd,
          scrub: true
        }
      }
    )
  })
  
  // If you ever change any of the animation props at runtime, refresh the trigger:
  watch(
    () => [
      props.animationDuration,
      props.ease,
      props.scrollStart,
      props.scrollEnd,
      props.stagger
    ],
    () => {
      ScrollTrigger.refresh()
    }
  )
  </script>


<style>
/* src/components/ScrollFloat.css */

.scroll-float {
  overflow: hidden;
  display: inline-block;
}

.scroll-float-text {
  display: inline-block;
}

.char {
  display: inline-block;
  white-space: pre; /* preserve spaces */
}

</style>