import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditpostviewComponent } from './editpostview.component';

describe('EditpostviewComponent', () => {
  let component: EditpostviewComponent;
  let fixture: ComponentFixture<EditpostviewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditpostviewComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EditpostviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
