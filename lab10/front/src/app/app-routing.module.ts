import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import{VacanciesComponent} from "./vacancies/vacancies.component";
import{CompaniesComponent} from "./companies/companies.component";

const routes: Routes = [
  {path: 'vacancies/:id', component: VacanciesComponent},
  {path: 'companies/:id', component: CompaniesComponent},
  {path: '', redirectTo: 'home', pathMatch: 'full'},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
