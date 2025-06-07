<template>
  <div
    :class="[
      'inline-block bg-clip-text text-transparent',
      disabled ? '' : 'animate-shine',
      className
    ]"
    :style="{
      backgroundImage: gradientString,
      backgroundSize: '200% 100%',
      animationDuration: animationDuration,
    }"
  >
    {{ text }}
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  text:       { type: String,  required: true },
  disabled:   { type: Boolean, default: false },
  speed:      { type: Number,  default: 3 },
  className:  { type: String,  default: '' },
  baseColor:  { type: String,  default: 'rgba(242, 242, 242, 1)' },  // #48894A
  shineColor: { type: String,  default: 'rgba(72, 137, 74, 0.8)' }, // fallback
});

// Compute “5s”, “3s”, etc.
const animationDuration = computed(() => `${props.speed}s`);

// Build a gradient where the “baseColor” is on either side, and the “shineColor” in the middle

// ${props.baseColor} 40%,${props.baseColor} 60%,

const gradientString = computed(() => {
  return `linear-gradient(
    120deg,
    ${props.baseColor}  0%,
    ${props.shineColor} 50%,
    
    ${props.baseColor} 100%
  )`;
});
</script>

<style scoped>
@keyframes shine {
  0%   { background-position: 200% ; }
  /* 30% { background-position: -100% ; }
  60% { background-position: -80% ; } */
  100% { background-position: -200% ; }
}
.animate-shine {
  animation: shine animationDuration ease-in-out infinite;
  background: linear-gradient(90deg, #fff 0%, #a855f7 50%, #fff 100%);
  background-size: 200% 100%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
