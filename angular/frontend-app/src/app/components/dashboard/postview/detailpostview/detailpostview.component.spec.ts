import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetailpostviewComponent } from './detailpostview.component';

describe('DetailpostviewComponent', () => {
  let component: DetailpostviewComponent;
  let fixture: ComponentFixture<DetailpostviewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DetailpostviewComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DetailpostviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
