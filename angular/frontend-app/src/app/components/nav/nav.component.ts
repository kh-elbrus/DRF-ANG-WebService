import { HttpClient } from '@angular/common/http';
import { EventEmitter } from '@angular/core';
import { Inject, Output } from '@angular/core';
import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatSlideToggle, MatSlideToggleChange } from '@angular/material/slide-toggle';
import { MatSnackBar } from '@angular/material/snack-bar';
import { AUTH_API_URL } from 'src/app/app-injection-tokens';
import { AuthService } from 'src/app/services/auth/auth.service';
import { UserinfoService } from 'src/app/services/data/userinfo.service';
import { AddnewpostComponent } from '../dashboard/addnewpost/addnewpost.component';


@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})
export class NavComponent implements OnInit {

  email: string = '';
  username: string = '';

  @Output()
  readonly darkModeSwitched = new EventEmitter<boolean>();

  public get isLoggedIn(): boolean {
    return this.as.isAuthenticated()
  }

  constructor(
    private as: AuthService,
    private http: HttpClient,
    @Inject(AUTH_API_URL) private apiUrl: string,
    private us: UserinfoService,
    private dialog: MatDialog,
  ) { }

  ngOnInit(): void {
    this.us.getUserinfo().subscribe(res => {
      this.email = res.email,
      this.username = res.name
    })    
  }

  logout() {
    this.as.logout()
  }

  addDialogNewPost() {
    this.dialog.open(AddnewpostComponent)
  }
  
}
