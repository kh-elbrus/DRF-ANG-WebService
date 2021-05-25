import { Component, Inject, Input, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { MatDialog, MatDialogModule, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Posts } from 'src/app/models/posts';
import { PostsService } from 'src/app/services/data/posts.service';
import { EditpostviewComponent } from '../editpostview/editpostview.component';

@Component({
  selector: 'app-detailpostview',
  templateUrl: './detailpostview.component.html',
  styleUrls: ['./detailpostview.component.scss']
})
export class DetailpostviewComponent implements OnInit {

  d_post: any;
  del_post: any;
  @Input() edit_id: any = this.route.snapshot.paramMap.get('id');;
  
  constructor(
    private ps: PostsService,
    private route:ActivatedRoute,
    private r_route:Router,
    private dialog:MatDialog,
    private fb: FormBuilder,
  ) { 
   }

  ngOnInit(): void {
    this.loadPost();
    
  }

  loadPost() {
    const postID = this.route.snapshot.paramMap.get('id');
    this.ps.getPostById(postID).subscribe(data => this.d_post = data)
  }

  deletePost() {
    const postID = this.route.snapshot.paramMap.get('id')
    this.ps.deletePostById(postID).subscribe(() => this.r_route.navigate(['/home']))
  }

  editPost() {
    this.dialog.open(EditpostviewComponent);
  //   const editPostComp = new EditpostviewComponent(this.fb, dialogRef);
  //   dialogRef.().subscribe(async res => {
  //     this.ps.editPostById(postID, editPostComp.editPostDialog()).subscribe(() => this.r_route.navigate([`/posts/:${postID}`]))
  //   } )
  // }
  }

  public retPostId(){
    const postID = this.route.snapshot.paramMap.get('id')
    return postID
  }

}