<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

const count = ref(0)
</script>

<template>

    <div class="border-solid rounded-lg border-2 border-borders-purple bg-sections-about_me bg-opacity-10 p-2 lg:p-10 md:p-6 ">
      <h1 class="capitalize">about me</h1>
      <div class="ml-6 m-4 max-w-2xl">
        <p class="mb-6">Hi, I'm Valeri. I'm a Backend Developer with Full-Stack skills and a strong foundation in Python, Django, React, and modern technologies like AWS and Docker. I’m based in Bat-Yam, Israel, with extensive experience in networking.</p>
        <p class="mb-6">I’m incredibly passionate about backend engineering, web application development, and creating full-stack solutions that are both functional and visually intuitive. I thrive on building large and complex projects, designing with purpose, and coding with passion.</p>
        <p class="mb-6">In my free time, I enjoy solving LeetCode problems, enhancing my skills with new frameworks and technologies, and working on real-world applications like my CRM Project.</p>
      </div>
    </div>


</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
