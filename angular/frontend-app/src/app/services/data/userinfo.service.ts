import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AUTH_API_URL } from 'src/app/app-injection-tokens';
import { User } from 'src/app/models/user';
import { ACCESS_TOKEN_KEY } from '../auth/auth.service';

const access_token = localStorage.getItem(ACCESS_TOKEN_KEY)

@Injectable({
  providedIn: 'root'
})
export class UserinfoService {
  private baseApiUrl = `${this.apiUrl}me/`

  constructor(
    private http: HttpClient,
    @Inject(AUTH_API_URL) private apiUrl: string
  ) { }

  getUserinfo(): Observable<User> {
    var header = {
      headers: new HttpHeaders()
        .set('Authorization',  `Bearer ${access_token}`)
    }
    return this.http.get<User>(`${this.baseApiUrl}`, header)
  }
}