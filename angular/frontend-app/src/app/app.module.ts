import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { NavComponent } from './components/nav/nav.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RegisterComponent } from './components/register/register.component';
import { AUTH_API_URL, STORE_API_URL } from './app-injection-tokens';
import { ACCESS_TOKEN_KEY } from './services/auth/auth.service';
import { environment } from 'src/environments/environment';
import { JwtModule, JWT_OPTIONS } from '@auth0/angular-jwt';
import { HttpClientModule } from '@angular/common/http';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatMenuModule } from '@angular/material/menu';
import { MatInputModule } from '@angular/material/input';
import { MatTabsModule } from '@angular/material/tabs';
import { MatSidenavModule } from '@angular/material/sidenav';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatCardModule} from '@angular/material/card';
import { FlexLayoutModule } from '@angular/flex-layout';
import {MatFormFieldModule} from '@angular/material/form-field';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { FooterComponent } from './components/footer/footer.component';
import { PostviewComponent } from './components/dashboard/postview/postview.component';
import { NavPaginatorComponent } from './components/dashboard/nav-paginator/nav-paginator.component';
import {MatPaginatorModule} from '@angular/material/paginator';
import {MatSlideToggleModule} from '@angular/material/slide-toggle';
import {MatSnackBarModule} from '@angular/material/snack-bar';
import {MatDialogModule} from '@angular/material/dialog';
import { DialognotificationComponent } from './components/login/dialognotification/dialognotification.component';
import { DetailpostviewComponent } from './components/dashboard/postview/detailpostview/detailpostview.component';
import { AddnewpostComponent } from './components/dashboard/addnewpost/addnewpost.component';
import { MatSelectModule } from '@angular/material/select';
import { EditpostviewComponent } from './components/dashboard/postview/editpostview/editpostview.component';


export function jwtOptionsFactory() {
  return {
    tokenGetter: () => {
      return localStorage.getItem(ACCESS_TOKEN_KEY);
    },
    whitelistedDomains: environment.tokenWhitelistedDomains
  }
}

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    NavComponent,
    DashboardComponent,
    RegisterComponent,
    FooterComponent,
    PostviewComponent,
    NavPaginatorComponent,
    DialognotificationComponent,
    DetailpostviewComponent,
    AddnewpostComponent,
    EditpostviewComponent,
  ],
  entryComponents: [
    DialognotificationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatButtonModule,
    MatIconModule,
    MatToolbarModule,
    MatMenuModule,
    MatInputModule,
    MatTabsModule,
    MatSidenavModule,
    MatSlideToggleModule,
    MatGridListModule,
    MatSelectModule,
    MatPaginatorModule,
    MatSnackBarModule,
    MatDialogModule,
    MatCardModule,
    FlexLayoutModule,
    MatFormFieldModule,
    FormsModule,
    ReactiveFormsModule,
    JwtModule.forRoot({
      jwtOptionsProvider: {
        provide: JWT_OPTIONS,
        useFactory: jwtOptionsFactory
      }
    })
  ],
  providers: [{
    provide: AUTH_API_URL,
    useValue: environment.authApi
  },{
    provide: STORE_API_URL,
    useValue: environment.storeApi
  }],
  bootstrap: [AppComponent]
})
export class AppModule { }
