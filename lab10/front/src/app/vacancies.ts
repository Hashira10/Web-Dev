export interface Vacancy {
  id: number;
  name: string;
  description: string;
  salary: number;
  company: string; // A reference to the parent company
  // Add any other fields you need here
}
