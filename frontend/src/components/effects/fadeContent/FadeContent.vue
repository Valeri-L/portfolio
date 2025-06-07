<template>
    <div
      ref="root"
      :class="className"
      :style="containerStyle"
    >
      <slot />
    </div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
  
  // Props definition
  const props = defineProps({
    blur: { type: Boolean, default: false },
    duration: { type: Number, default: 1000 },  // in ms
    easing: { type: String, default: 'ease-out' },
    delay: { type: Number, default: 0 },        // in ms
    threshold: { type: Number, default: 0.1 },
    initialOpacity: { type: Number, default: 0 },
    className: { type: String, default: '' }
  })
  
  // Reactive state
  const inView = ref(false)
  const root = ref(null)
  let observer = null
  
  onMounted(() => {
    if (!root.value) return
    observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          observer.unobserve(root.value)
          setTimeout(() => {
            inView.value = true
          }, props.delay)
        }
      },
      { threshold: props.threshold }
    )
    observer.observe(root.value)
  })
  
  onBeforeUnmount(() => {
    if (observer) observer.disconnect()
  })
  
  // Computed style based on inView
  const containerStyle = computed(() => ({
    opacity: inView.value ? 1 : props.initialOpacity,
    transition: `opacity ${props.duration}ms ${props.easing}${props.blur ? `, filter ${props.duration}ms ${props.easing}` : ''}`,
    filter: props.blur
      ? inView.value
        ? 'blur(0px)'
        : 'blur(10px)'
      : 'none'
  }))
  </script>
  
  <style scoped>
  /* No default styles; use className prop for styling as needed */
  </style>
  