import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit, Inject, EventEmitter } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { ACCESS_TOKEN_KEY } from 'src/app/services/auth/auth.service';
import { PostsService } from 'src/app/services/data/posts.service';

const access_token = localStorage.getItem(ACCESS_TOKEN_KEY)

@Component({
  selector: 'app-addnewpost',
  templateUrl: './addnewpost.component.html',
  styleUrls: ['./addnewpost.component.scss']
})
export class AddnewpostComponent implements OnInit {

  form!: FormGroup;
  
  constructor(
    public dialogRef: MatDialogRef<AddnewpostComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
    public ps: PostsService,
    private http: HttpClient,
    private formBuilder: FormBuilder,
    private router: Router
  ) { }

  onNoClick(): void {
    this.dialogRef.close();
  }

  onSubmit(): void {

    var header = {
      headers: new HttpHeaders()
        .set('Authorization',  `Bearer ${access_token}`)
    }

    console.log(this.form.getRawValue());
    this.http.post('http://localhost:8000/api/v1/article/posts/', this.form.getRawValue(), header)
    .subscribe(() => this.router.navigate(['/home']));
  }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      title: '',
      // preview: new FormControl(null, [Validators.required, requiredFileType('png')]),
      description: '',
      body: '',
      link: '',
      tags: this.formBuilder.array([]),
      technologies: this.formBuilder.array([])
    });
  }
}

function requiredFileType(arg0: string): import("@angular/forms").ValidatorFn {
  throw new Error('Function not implemented.');
}
