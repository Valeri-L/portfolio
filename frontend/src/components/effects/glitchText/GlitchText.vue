<template>
    <div
      :style="inlineStyles"
      :data-text="text"
      :class="combinedClasses"
    >
      {{ text }}
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue';
  
  // ---------------
  // 1) Props
  // ---------------
  const props = defineProps({
    text: {
      type: String,
      required: true,
    },
    speed: {
      type: Number,
      default: 0.5, // seconds
    },
    enableShadows: {
      type: Boolean,
      default: true,
    },
    enableOnHover: {
      type: Boolean,
      default: false,
    },
    className: {
      type: String,
      default: '',
    },
  });
  
  // ---------------
  // 2) Inline CSS variables for durations & shadows
  // ---------------
  const inlineStyles = computed(() => {
    return {
      '--after-duration': `${props.speed * 3}s`,
      '--before-duration': `${props.speed * 2}s`,
      '--after-shadow': props.enableShadows ? '-5px 0 red' : 'none',
      '--before-shadow': props.enableShadows ? '5px 0 cyan' : 'none',
    };
  });
  
  // ---------------
  // 3) Base Tailwind classes + pseudo‐classes
  // ---------------
  const baseClasses =
    'text-white text-[clamp(.4rem,2vw,1.2rem)] font-black relative mx-auto select-none cursor-pointer';
  
  const pseudoClasses = computed(() => {
    if (!props.enableOnHover) {
      // Always‐on glitch
      return [
        // AFTER pseudo
        "after:content-[attr(data-text)]",
        'after:absolute',
        'after:top-0',
        'after:left-[10px]',
        'after:text-white',
        'after:bg-[#060606]',
        'after:overflow-hidden',
        'after:[clip-path:inset(0_0_0_0)]',
        'after:[text-shadow:var(--after-shadow)]',
        'after:animate-glitch-after',
        // BEFORE pseudo
        "before:content-[attr(data-text)]",
        'before:absolute',
        'before:top-0',
        'before:left-[-10px]',
        'before:text-white',
        'before:bg-[#060606]',
        'before:overflow-hidden',
        'before:[clip-path:inset(0_0_0_0)]',
        'before:[text-shadow:var(--before-shadow)]',
        'before:animate-glitch-before',
      ].join(' ');
    } else {
      // Only glitch on hover
      return [
        // AFTER (initially hidden)
        "after:content-['']",
        'after:absolute',
        'after:top-0',
        'after:left-[10px]',
        'after:text-white',
        'after:bg-[#060606]',
        'after:overflow-hidden',
        'after:[clip-path:inset(0_0_0_0)]',
        'after:opacity-0',
        // BEFORE (initially hidden)
        "before:content-['']",
        'before:absolute',
        'before:top-0',
        'before:left-[-10px]',
        'before:text-white',
        'before:bg-[#060606]',
        'before:overflow-hidden',
        'before:[clip-path:inset(0_0_0_0)]',
        'before:opacity-0',
        // On hover – reveal AFTER
        'hover:after:content-[attr(data-text)]',
        'hover:after:opacity-100',
        'hover:after:[text-shadow:var(--after-shadow)]',
        'hover:after:animate-glitch-after',
        // On hover – reveal BEFORE
        'hover:before:content-[attr(data-text)]',
        'hover:before:opacity-100',
        'hover:before:[text-shadow:var(--before-shadow)]',
        'hover:before:animate-glitch-before',
      ].join(' ');
    }
  });
  
  // ---------------
  // 4) Combine everything
  // ---------------
  const combinedClasses = computed(() => {
    return [baseClasses, pseudoClasses.value, props.className].filter(Boolean).join(' ');
  });
  </script>
  
  <style scoped>
  /* --------------- */
  /* 5) Tailwind keyframes & animation */
  /* --------------- */
  
  @keyframes glitch {
    0%   { clip-path: inset(20% 0 50% 0); }
    5%   { clip-path: inset(10% 0 60% 0); }
    10%  { clip-path: inset(15% 0 55% 0); }
    15%  { clip-path: inset(25% 0 35% 0); }
    20%  { clip-path: inset(30% 0 40% 0); }
    25%  { clip-path: inset(40% 0 20% 0); }
    30%  { clip-path: inset(10% 0 60% 0); }
    35%  { clip-path: inset(15% 0 55% 0); }
    40%  { clip-path: inset(25% 0 35% 0); }
    45%  { clip-path: inset(30% 0 40% 0); }
    50%  { clip-path: inset(20% 0 50% 0); }
    55%  { clip-path: inset(10% 0 60% 0); }
    60%  { clip-path: inset(15% 0 55% 0); }
    65%  { clip-path: inset(25% 0 35% 0); }
    70%  { clip-path: inset(30% 0 40% 0); }
    75%  { clip-path: inset(40% 0 20% 0); }
    80%  { clip-path: inset(20% 0 50% 0); }
    85%  { clip-path: inset(10% 0 60% 0); }
    90%  { clip-path: inset(15% 0 55% 0); }
    95%  { clip-path: inset(25% 0 35% 0); }
    100% { clip-path: inset(30% 0 40% 0); }
  }
  
  .animate-glitch-after {
    animation: glitch var(--after-duration) infinite linear alternate-reverse;
  }
  .animate-glitch-before {
    animation: glitch var(--before-duration) infinite linear alternate-reverse;
  }
  </style>
  