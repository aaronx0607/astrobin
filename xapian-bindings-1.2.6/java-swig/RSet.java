/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.5
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */


public class RSet {
  private long swigCPtr;
  protected boolean swigCMemOwn;

  public RSet(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  public static long getCPtr(RSet obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        XapianJNI.delete_RSet(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public RSet(RSet other) {
    this(XapianJNI.new_RSet__SWIG_0(RSet.getCPtr(other), other), true);
  }

  public RSet() {
    this(XapianJNI.new_RSet__SWIG_1(), true);
  }

  public long size() {
    return XapianJNI.RSet_size(swigCPtr, this);
  }

  public boolean empty() {
    return XapianJNI.RSet_empty(swigCPtr, this);
  }

  public void addDocument(long did) {
    XapianJNI.RSet_addDocument__SWIG_0(swigCPtr, this, did);
  }

  public void addDocument(MSetIterator i) {
    XapianJNI.RSet_addDocument__SWIG_1(swigCPtr, this, MSetIterator.getCPtr(i), i);
  }

  public void removeDocument(long did) {
    XapianJNI.RSet_removeDocument__SWIG_0(swigCPtr, this, did);
  }

  public void removeDocument(MSetIterator i) {
    XapianJNI.RSet_removeDocument__SWIG_1(swigCPtr, this, MSetIterator.getCPtr(i), i);
  }

  public boolean contains(long did) {
    return XapianJNI.RSet_contains__SWIG_0(swigCPtr, this, did);
  }

  public boolean contains(MSetIterator i) {
    return XapianJNI.RSet_contains__SWIG_1(swigCPtr, this, MSetIterator.getCPtr(i), i);
  }

  public String toString() {
    return XapianJNI.RSet_toString(swigCPtr, this);
  }

}
