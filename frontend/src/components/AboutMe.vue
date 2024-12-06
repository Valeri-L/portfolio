<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

const count = ref(0)
</script>

<template>

  <div class="border-solid border-2 border-sky-500">
    <p>about me information</p>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis hic aspernatur perferendis sit earum commodi ut nemo quae maiores natus quam est obcaecati delectus nulla laboriosam placeat ratione, molestias sapiente.</p>
  </div>


</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
