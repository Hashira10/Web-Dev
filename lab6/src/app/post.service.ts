import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Album} from "./models";
@Injectable({
  providedIn: 'root'
})
export class PostService {
  constructor(private client: HttpClient) { }

  getPosts(): Observable<Album[]>{
    return this.client.get<Album[]>('https://jsonplaceholder.typicode.com/posts');
  }

  getPost(id: number): Observable<Album>{
    return this.client.get<Album>(`https://jsonplaceholder.typicode.com/posts/${id}`)
  }
}
