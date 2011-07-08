/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.5
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */


public class PositionIterator {
  private long swigCPtr;
  protected boolean swigCMemOwn;

  public PositionIterator(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  public static long getCPtr(PositionIterator obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        XapianJNI.delete_PositionIterator(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public PositionIterator() {
    this(XapianJNI.new_PositionIterator__SWIG_0(), true);
  }

  public PositionIterator(PositionIterator other) {
    this(XapianJNI.new_PositionIterator__SWIG_1(PositionIterator.getCPtr(other), other), true);
  }

  public long getTermPos() {
    return XapianJNI.PositionIterator_getTermPos(swigCPtr, this);
  }

  public long next() {
    return XapianJNI.PositionIterator_next(swigCPtr, this);
  }

  public boolean equals(PositionIterator other) {
    return XapianJNI.PositionIterator_equals(swigCPtr, this, PositionIterator.getCPtr(other), other);
  }

  public void skipTo(long pos) {
    XapianJNI.PositionIterator_skipTo(swigCPtr, this, pos);
  }

  public String toString() {
    return XapianJNI.PositionIterator_toString(swigCPtr, this);
  }

}
