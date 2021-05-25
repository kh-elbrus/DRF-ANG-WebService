import { HttpClient } from '@angular/common/http';
import { Token } from '@angular/compiler/src/ml_parser/lexer';
import { Inject, Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { AUTH_API_URL } from 'src/app/app-injection-tokens';

export const ACCESS_TOKEN_KEY = 'access';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(
    private http: HttpClient,
    @Inject(AUTH_API_URL) private apiUrl: string,
    private jwtHelper: JwtHelperService,
    private router: Router
  ) { }

  login(email: string, password: string): Observable<Token>{
    return this.http.post<Token>(`${this.apiUrl}token/`, {
      email, password
    }).pipe(
      tap((token: any) => {
        console.log(token);
        console.log(token.access);
        localStorage.setItem(ACCESS_TOKEN_KEY, token.access);
      })
    )
  }

  isAuthenticated(): boolean {
    var token = localStorage.getItem(ACCESS_TOKEN_KEY); 
    return token != null && !this.jwtHelper.isTokenExpired(token)
  }

  logout(): void {
    localStorage.removeItem(ACCESS_TOKEN_KEY);
    this.router.navigate(['login/'])
  }
}