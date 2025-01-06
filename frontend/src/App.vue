<template>

  <!-- Main content area where components will be displayed -->
  <div class="bg-primary-200 mx-4 md:mx-10 lg:mx-20 md:p-0 rounded-lg shadow-lg mt-[180px]">
    <!-- Only this part should be rendered dynamically, based on the route -->
    <router-view></router-view>
  </div>
</template>

<script setup>
// import NavigationBar from './components/NavigationBar.vue';
</script>

<style scoped>
/* Your styles here */
</style>
