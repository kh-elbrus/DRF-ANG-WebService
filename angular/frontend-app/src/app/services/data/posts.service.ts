import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { AUTH_API_URL, STORE_API_URL } from 'src/app/app-injection-tokens';
import { Posts } from 'src/app/models/posts';
import { ACCESS_TOKEN_KEY } from '../auth/auth.service';

const access_token = localStorage.getItem(ACCESS_TOKEN_KEY)

@Injectable({
  providedIn: 'root'
})
export class PostsService {

  model!: Posts; 
  private baseApiUrl = `${this.apiUrl}posts/`
  private baseApiUrlCat = `${this.apiUrl}technologies/`
  private baseApiUrlTag = `${this.apiUrl}tags/`

  constructor(
    private http: HttpClient,
    @Inject(STORE_API_URL) private apiUrl: string
  ) { }

  getPosts(): Observable<Posts[]> {
    var header = {
      headers: new HttpHeaders()
        .set('Authorization',  `Bearer ${access_token}`)
    }
    return this.http.get<Posts[]>(`${this.baseApiUrl}`, header)
  }

  getPostById(id: any): Observable<any>{
    var header = {
      headers: new HttpHeaders()
        .set('Authorization',  `Bearer ${access_token}`)
    }
    return this.http.get(`${this.baseApiUrl}${id}/`, header)
  }

  addPost(data: any): void {
    var header = {
      headers: new HttpHeaders()
        .set('Authorization',  `Bearer ${access_token}`)
    }
    this.http.post(`${this.baseApiUrl}`, data, header)
  }
  getCategories(): Observable<any>{
    var header = {
      headers: new HttpHeaders()
        .set('Authorization',  `Bearer ${access_token}`)
    }
    return this.http.get<any>(`${this.baseApiUrlCat}`, header)
  }

  getTags(): void{
    var header = {
      headers: new HttpHeaders()
        .set('Authorization',  `Bearer ${access_token}`)
    }
    this.http.get(`${this.baseApiUrlTag}`, header)
  }

  deletePostById(id: any): Observable<any> {
    var header = {
      headers: new HttpHeaders()
        .set('Authorization',  `Bearer ${access_token}`)
    }
    return this.http.delete(`${this.baseApiUrl}${id}/`, header)
  }

  editPostById(id: any, data: any): Observable<any> {
    var header = {
      headers: new HttpHeaders()
        .set('Authorization',  `Bearer ${access_token}`)
    }
    return this.http.put(`${this.baseApiUrl}${id}/`, data, header)
  }

}
