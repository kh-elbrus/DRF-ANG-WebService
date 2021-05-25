import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { PostsService } from 'src/app/services/data/posts.service';
import { ActivatedRoute, Router } from '@angular/router';
import { MatDialogRef } from '@angular/material/dialog';
import { DetailpostviewComponent } from '../detailpostview/detailpostview.component';

@Component({
  selector: 'app-editpostview',
  templateUrl: './editpostview.component.html',
  styleUrls: ['./editpostview.component.scss']
})
export class EditpostviewComponent implements OnInit {

  form!: FormGroup;
  post_edit_id!: any;

  constructor(
    private fb: FormBuilder,
    public dialogRef: MatDialogRef<EditpostviewComponent>,
    private router: ActivatedRoute,
    private ps: PostsService,
    private r_router: Router,
  ) { }

  ngOnInit(): void {
    this.form = this.fb.group({
      title: '',
      // preview: new FormControl(null, [Validators.required, requiredFileType('png')]),
      description: '',
      body: '',
      link: '',
      tags: this.fb.array([]),
      technologies: this.fb.array([])
    });
  }

  // async editPostDialog(): Promise<void>{
  //   return this.form.getRawValue()
    
  // }
  retPostId() {
    this.router.paramMap.subscribe(params => { 
      this.post_edit_id = params.get('id'); 
  });
  }

  editPostDialog(): void{
    const postID = this.post_edit_id
    const postData = this.form.getRawValue()
    console.log(this.form.getRawValue());
    
    this.ps.editPostById(postID, postData).subscribe(() => this.r_router.navigate([`/posts/:${postID}`]))
  }
  
  onNoClick(): void {
    return this.dialogRef.close();
  }
  
}

function requiredFileType(arg0: string): import("@angular/forms").ValidatorFn {
  throw new Error('Function not implemented.');
}
