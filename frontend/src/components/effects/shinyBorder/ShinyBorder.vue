<template>
    <component
      :is="as"
      :class="['star-border-container', className]"
      v-bind="restAttrs"
    >
      <!-- Bottom-moving gradient circle -->
      <div
        class="border-gradient-bottom"
        :style="gradientStyle"
      ></div>
  
      <!-- Top-moving gradient circle -->
      <div
        class="border-gradient-top"
        :style="gradientStyle"
      ></div>
  
      <!-- Content slot -->
      <div class="inner-content">
        <slot />
      </div>
    </component>
  </template>
  
  <script setup>
  import { defineProps, useAttrs, computed } from 'vue'
  
  const props = defineProps({
    as: { type: String, default: 'button' },
    className: { type: String, default: '' },
    color: { type: String, default: 'white' },
    speed: { type: String, default: '6s' },
  })
  
  // Forward all other attributes (e.g., type="submit")
  const restAttrs = useAttrs()
  
  // Shared gradient + duration style
  const gradientStyle = computed(() => ({
    background: `radial-gradient(circle, ${props.color}, transparent 10%)`,
    animationDuration: props.speed
  }))
  </script>
  
  <style>
  .star-border-container {
    position: relative;
    display: inline-block;
    padding: 1px;
    overflow: hidden;
    border-radius: 20px;
  }
  
  .border-gradient-bottom,
  .border-gradient-top {
    position: absolute;
    width: 300%;
    height: 50%;
    opacity: 0.7;
    border-radius: 50%;
    z-index: 0;
  }
  
  .border-gradient-bottom {
    bottom: -11px;
    right: -250%;
    animation-name: starMovementBottom;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
    animation-direction: alternate;
  }
  
  .border-gradient-top {
    top: -10px;
    left: -250%;
    animation-name: starMovementTop;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
    animation-direction: alternate;
  }
  
  .inner-content {
    position: relative;
    z-index: 1;
    background: linear-gradient(to bottom, #000000, #333333);
    border: 1px solid #222222;
    color: #ffffff;
    text-align: center;
    font-size: 16px;
    padding: 16px 26px;
    border-radius: 20px;
  }
  
  @keyframes starMovementBottom {
    0% { transform: translate(0%, 0%); opacity: 1; }
    100% { transform: translate(-100%, 0%); opacity: 0; }
  }
  
  @keyframes starMovementTop {
    0% { transform: translate(0%, 0%); opacity: 1; }
    100% { transform: translate(100%, 0%); opacity: 0; }
  }
  </style>
  