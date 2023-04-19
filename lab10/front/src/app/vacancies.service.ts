import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Vacancy} from "./vacancies";

@Injectable({
  providedIn: 'root'
})
export class VacancyService {
  constructor(private client: HttpClient) {
  }
  BASE_URL = 'http://localhost:8000';

  getVacancy(): Observable<Vacancy[]> {
    return this.client.get<Vacancy[]>(`${this.BASE_URL}/api/vacancies/`);
  }

  getVacancyDetail(id: string): Observable<Vacancy> {
    return this.client.get<Vacancy>(`${this.BASE_URL}/api/vacancies/${id}/`);
  }

  getVacancyByCompanyId(id: any): Observable<Vacancy[]> {
    return this.client.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${id}/vacancies`);
  }
}
