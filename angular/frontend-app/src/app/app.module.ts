import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MenubarComponent } from './menubar/menubar.component';
import { MatMenuModule } from '@angular/material/menu';
import { MatInputModule } from '@angular/material/input';
import { MatTabsModule } from '@angular/material/tabs';
import { FooterbarComponent } from './footerbar/footerbar.component';
import { MatSidenavModule } from '@angular/material/sidenav';
import { PostviewComponent } from './postview/postview.component';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatCardModule} from '@angular/material/card';
import { FlexLayoutModule } from '@angular/flex-layout';
import { LoginsideComponent } from './loginside/loginside.component';
import { RegistrationsideComponent } from './registrationside/registrationside.component';
import { AddnewarticleComponent } from './addnewarticle/addnewarticle.component';
import { ProfileComponent } from './profile/profile.component';
import { AddnewcategoryComponent } from './addnewcategory/addnewcategory.component';
import { HomesideComponent } from './homeside/homeside.component';
import { ArticlesideComponent } from './articleside/articleside.component';
import {MatFormFieldModule} from '@angular/material/form-field';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    AppComponent,
    MenubarComponent,
    FooterbarComponent,
    PostviewComponent,
    LoginsideComponent,
    RegistrationsideComponent,
    AddnewarticleComponent,
    ProfileComponent,
    AddnewcategoryComponent,
    HomesideComponent,
    ArticlesideComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatIconModule,
    MatToolbarModule,
    MatMenuModule,
    MatInputModule,
    MatTabsModule,
    MatSidenavModule,
    MatGridListModule,
    MatCardModule,
    FlexLayoutModule,
    MatFormFieldModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
