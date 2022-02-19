<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8 main-header">
        <h2><router-link to="/index">Todo List</router-link></h2>
        <router-link to="/create" class="btn btn-sm btn-primary">Add Task</router-link>
        <router-link to="/index" class="btn btn-sm btn-secondary task-b">Back to list</router-link>
      
        <router-view />
      </div>
    </div>
  </div>
</template>

<style lang="css">
  .main-header{
    padding-top: 20px;
    margin: 20px;
  }
  .main-header h2{
    font-size: 40px;
    font-weight: bolder;
  }
  
@media only screen and (min-width: 768px) {
  .main-header{
    padding-top: 20px;
    margin: 20px;
  }
    
  }
</style>