import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginsideComponent } from './loginside.component';

describe('LoginsideComponent', () => {
  let component: LoginsideComponent;
  let fixture: ComponentFixture<LoginsideComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LoginsideComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginsideComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
