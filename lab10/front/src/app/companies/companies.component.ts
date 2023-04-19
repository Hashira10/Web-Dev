import { Component } from '@angular/core';
import {Vacancy} from "../vacancies";
import {Company} from "../companies";
import {VacancyService} from "../vacancies.service";
import {CompanyService} from "../companies.service";
import {ActivatedRoute, Router} from "@angular/router";
@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent {
  vacancies: Vacancy[] = [];
  company!: Company;

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private vouchersService: VacancyService,
    private categoriesService: CompanyService
  ) {
  }


  ngOnInit(): void {
    this.getCompany();
    this.getVacancy();
  }

  getVacancy(): void {
    this.route.paramMap.subscribe((params) => {
      const id = params.get('id');
      if (id !== null) {
        this.vouchersService.getVacancyByCompanyId(id).subscribe((data) => {
          this.vacancies = data;
          console.log(data);
        });
      }
    });
  }

  getCompany(): void {
    this.route.paramMap.subscribe((params) => {
      const id = params.get('id');
      if (id !== null) {
        this.categoriesService.getCompany(id).subscribe((data) => {
          this.company = data;
          console.log(data);
        });
      }
    });
  }
}
