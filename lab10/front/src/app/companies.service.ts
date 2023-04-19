import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Company} from "./companies";
import {Observable} from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  BASE_URL = 'http://localhost:8000';

  constructor(private client: HttpClient) { }

  getCompany(id: any): Observable<Company> {
    return this.client.get<Company>(`${this.BASE_URL}/api/companies/${id}/`);
  }

  getCategories(): Observable<Company[]> {
    return this.client.get<Company[]>(`${this.BASE_URL}/api/companies/`);
  }
}
