<template>
  <div>
    <h3 class="mb-4">Patient Details Form</h3>
    <form>
      <div class="mb-3">
        <label for="name" class="form-label">Patient Name</label>
        <input
          type="text"
          class="form-control"
          id="name"
          placeholder="Enter patient's name"
        />
      </div>
      <div class="mb-3">
        <label for="dob" class="form-label">Date of Birth</label>
        <input type="date" class="form-control" id="dob" />
      </div>
      <div class="mb-3">
        <label for="contact" class="form-label">Contact Information</label>
        <input
          type="text"
          class="form-control"
          id="contact"
          placeholder="Enter contact details"
        />
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "PatientDetailsForm",
};
</script>

<style scoped>
/* Add any specific styles for the form here */
</style>
