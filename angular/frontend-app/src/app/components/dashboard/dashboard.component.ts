import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth/auth.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  public get isLoggedIn(): boolean {
    return this.as.isAuthenticated()
  }

  constructor(private as: AuthService) { }

  ngOnInit(): void {
  }

}
