function getNumberOfDepartments(employeesList) {
  return Object.keys(employeesList).length;
}

export default function createReportObject(employeesList) {
  return {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments,
  };
}
