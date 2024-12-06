<script setup>
import { ref } from 'vue'
import colors from '../assets/styles/main'

const count = ref(0)
const button_sx = `bg-transparent border-none hover:underline underline-offset-8 decoration-text-purple`
</script>

<template>

  <div class="border-b-2 mb-5" :style="{borderColor:colors.borders.grey}">
    <div class="font-pixelify flex">

        <div class="flex-none ">
            <button :class="button_sx">Valeri Levinson</button><!-- logo on the top left side -->
            
            <!-- icons -->
            <button :class="button_sx">gt</button>
            <button :class="button_sx">in</button>
            <button :class="button_sx">m</button>
        </div>

        <div class="flex-none">
            <button :class="button_sx">about me</button>
            <button :class="button_sx">achievements</button>
            <button :class="button_sx">projects</button>
            <button :class="button_sx">contact me</button>
        </div>
        
    </div>
</div>


</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
