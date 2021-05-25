import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth/auth.service';
import {MatDialog} from '@angular/material/dialog';
import { DialognotificationComponent } from './dialognotification/dialognotification.component';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  durationInSeconds = 3;

  public get isLoggedIn(): boolean {
    return this.as.isAuthenticated()
  }

  constructor(
    private as: AuthService,
    private router: Router,
    public _snackBar: MatSnackBar
  ) { }

  ngOnInit(): void {
  }

  login(email: string, password: string) {
    this.as.login(email, password).subscribe(res => {
      this.router.navigate([''])
    }, error => {
      this._snackBar.open('Login Faild', 'Close', {
        duration: this.durationInSeconds * 1000,
        panelClass: ['mat-warn']
      });
    })
  }

}
