/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.5
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */


public class Stopper {
  private long swigCPtr;
  protected boolean swigCMemOwn;

  public Stopper(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  public static long getCPtr(Stopper obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        XapianJNI.delete_Stopper(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  protected void swigDirectorDisconnect() {
    swigCMemOwn = false;
    delete();
  }

  public void swigReleaseOwnership() {
    swigCMemOwn = false;
    XapianJNI.Stopper_change_ownership(this, swigCPtr, false);
  }

  public void swigTakeOwnership() {
    swigCMemOwn = true;
    XapianJNI.Stopper_change_ownership(this, swigCPtr, true);
  }

  public boolean apply(String term) {
    return XapianJNI.Stopper_apply(swigCPtr, this, term);
  }

  public String toString() {
    return (getClass() == Stopper.class) ? XapianJNI.Stopper_toString(swigCPtr, this) : XapianJNI.Stopper_toStringSwigExplicitStopper(swigCPtr, this);
  }

  public Stopper() {
    this(XapianJNI.new_Stopper(), true);
    XapianJNI.Stopper_director_connect(this, swigCPtr, swigCMemOwn, true);
  }

}
