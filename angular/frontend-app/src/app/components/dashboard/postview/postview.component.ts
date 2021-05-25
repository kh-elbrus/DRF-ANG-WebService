import { HttpClient } from '@angular/common/http';
import { Component, OnInit, Output } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { Posts } from 'src/app/models/posts';
import { PostsService } from 'src/app/services/data/posts.service';
import { DetailpostviewComponent } from './detailpostview/detailpostview.component';


@Component({
  selector: 'app-postview',
  templateUrl: './postview.component.html',
  styleUrls: ['./postview.component.scss']
})
export class PostviewComponent implements OnInit {

  views: number = 0;
  models!: Posts;
  post: Posts[] = [];
  colums = ['id', 'title', 'preview', 'description']

  constructor(
    private ps: PostsService,
    private router: Router,
    public dialog: MatDialog

  ) { }

  ngOnInit(): void {
    this.getPostList()
  }

  openPost(): void {
    const dialogRef = this.dialog.open(DetailpostviewComponent);

    dialogRef.afterClosed().subscribe(result => {
      this.views ++
    });
  }

  getPostList(): void {
    this.ps.getPosts().subscribe(res => {this.post = res})
  }

}
