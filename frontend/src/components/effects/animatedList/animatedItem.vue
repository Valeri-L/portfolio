<template>
    <div
      ref="el"
      class="item-wrapper"
      :class="{ selected }"
      @mouseenter="$emit('mouseenter')"
      @click="$emit('click')"
      :style="{
        transitionDelay: delay + 's',
        transform: inView ? 'scale(1)' : 'scale(0.2)',
        opacity:    inView ? 1         : 0
      }"
    >
      <slot />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  
  const props = defineProps({
    index:    Number,
    delay:    { type: Number, default: 0 },
    selected: { type: Boolean, default: false }
  })
  const emit = defineEmits(['mouseenter','click'])
  
  const el     = ref(null)
  const inView = ref(false)
  
  onMounted(() => {
    const obs = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          inView.value = true
          obs.unobserve(el.value)
        }
      },
      { threshold: 0.5 }
    )
    obs.observe(el.value)
  })
  </script>
  
  <style scoped>
  .item-wrapper {
    margin-bottom: 1rem;
    cursor: pointer;
    transition: transform 1.2s ease, opacity 1.2s ease;
  }
  .item-wrapper.selected {
    font-weight: bold;
    color: #C778DD;
  }
  </style>
  