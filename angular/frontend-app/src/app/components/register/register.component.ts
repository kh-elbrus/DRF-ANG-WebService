import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  public get isLoggedIn(): boolean {
    return this.as.isAuthenticated()
  }

  form!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router,
    private as: AuthService,

  ) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      name: '',
      email: '',
      password: '',
    });
  }

  submit(): void {
    console.log(this.form.getRawValue());
    this.http.post('http://localhost:8000/api/v1/user/create/', this.form.getRawValue())
    .subscribe(() => this.router.navigate(['/login']));
    }

}
